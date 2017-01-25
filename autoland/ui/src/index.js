/*
  TODO:
    -  Move components to their own files when we get updated paylaods from Steven
    -  Trigger controller refresh upon landing click
    -  Linkify commit descriptions to Reviewboard
    -  Linkify "View on Reviewboard" button
    -  Add error handling every step of the way
    -  Implement real fetch endpoints

    -  Should we automatically refresh the data every minute or so?
*/

import React from 'react';
import { render } from 'react-dom';

// Settings
const AUTOLAND_ENDPOINT = '...';
const AUTOLAND_POST_ENDPOINT = '...';

class ActionButtons extends React.Component {
  constructor(props) {
    super(props);
    this.state = { landing: false };
    this.onLandClick = this.onLandClick.bind(this);
  }

  onLandClick(e) {
    e.preventDefault();
    if (this.state.landing) {
      return;
    }
    this.setState({ landing: true });
  }

  render() {
    return (
      <div className="commit-buttons">
        {this.props.landable &&
          <a href=""
            onClick={this.onLandClick}
            className="land">{this.state.landing ? 'Landing Commits...' : 'Land Commits'}</a>
        }
        <a href={`https://bugzilla.mozilla.org/show_bug.cgi?id=${this.props.bug}`}>View on Bugzilla</a>
        <a href="">View on Reviewboard</a>
      </div>
    );
  }
}

class CommitsTable extends React.Component {
  render() {
    return (<ul className="commits-table">
      {this.props.commits.map(commit => (
        <li key={commit.revision}>
          <div className="commit-description"><a href="">{commit.description || 'Commit Description Here'}</a></div>
          <div className="commit-meta">
            <div className="commit-hash">{commit.revision}</div> - <div className="commit-author">{this.props.revisions[commit.revision].author}</div>
          </div>
          <div className="commit-reviewers">
            Reviewers:
            {commit.reviews.map(review => (
              <a href={`mailto: ${review.reviewer.email}`} data-status={review.status} key={review.reviewer.nick} className="commit-reviewer">
                <span className="commit-status">{review.status}</span> {review.reviewer.name}
              </a>
            ))}
          </div>
          <br />
          <div className="commit-notification">
            {commit.landing_blocker || (this.props.failures[commit.revision] ? `Landing failed: ${this.props.failures[commit.revision].error}` : '')}
          </div>
        </li>
      ))}
    </ul>);
  }
}

// This is the main controller/wrapper for the entire app
class Controller extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: null };
  }

  componentDidMount() {
    this.fetch();
  }

  fetch() {
    fetch(this.props.url).then(response => response.json()).then(data => {
      this.setState({ data });
    });
  }

  sendPost() {
    fetch(AUTOLAND_POST_ENDPOINT, { method: 'post', mode: 'cors' })
    .then(response => response.json())
    .then(data => {
      /* What to do? */
      if (data) { return; }
      if (this) { return; }
    });
  }

  render() {
    const data = this.state.data;

    // This is the default text for the element while we fetch data
    // during the initial widget creation
    if (data === null) {
      return <div>Fetching data...</div>;
    }

    // For now, the only push that matters is the first provided back
    const push = data.pushes && data.pushes[0];
    const landing = data.landings && data.landings[0];
    const failures = {};
    let failureCount = 0;

    // Messages blurbs based on current state of the push information
    // Defaulting to "all good, here's what you want to land"
    let message = (
      <div>
        <h2>Everything looks good!</h2>
        <p>About to land {push.commits.length} commits
        to <strong>{data.repository}</strong>.<br/>
        Please confirm these commit descriptions are correct
        before landing.<br/>
        If corrections are required, please amend the
        commit message and try again.</p>
      </div>
    );
    if (push.landing_blocker !== null) {
      switch (push.landing_blocker) {
        case 'Some commits are not ready to land.':
        case 'Already landed':
          message = <h2 className="error">{push.landing_blocker}</h2>;
          break;
        case 'Landing is already in progress':
          message = <h2>{push.landing_blocker}</h2>;
          break;
        default:
          message = <h2 className="error">Unrecognized response, please report!</h2>;
      }
    } else if (data.landings && data.landings[0]) {
      Object.keys(landing).forEach(landingId => {
        if (landing[landingId].status === 'failed') {
          failures[landingId] = landing[landingId];
        }
      });
      failureCount = Object.keys(failures).length;

      if (failureCount) {
        message = (
          <h2 className="error">
            Landing failed: {failureCount} failure{failureCount > 1 ? 's' : ''}.
          </h2>
        );
      }
    }

    const landable = (failureCount === 0 && push.landing_blocker === null);

    return (
      <div>
          {message}
          <CommitsTable
            commits={push.commits}
            failures={failures}
            revisions={data.revisions} />
          <ActionButtons landable={landable} bug={data.bug} />
      </div>
    );
  }
}

// Create the example elements
document.querySelectorAll('.instance').forEach(node => {
  const url = node.getAttribute('data-url') || AUTOLAND_ENDPOINT;
  render(<Controller url={url} />, node);
});
