import React from 'react';

import CommitsTable from './CommitsTable';
import ActionButtons from './ActionButtons';

const AUTOLAND_POST_ENDPOINT = '...';

class AutolandController extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: null };
  }

  componentDidMount() {
    this.fetch(this.props.params.series_id);
  }

  componentWillReceiveProps(nextProps) {
    if (this.props.params.series_id !== nextProps.params.series_id) {
      this.fetch(nextProps.params.series_id);
    }
  }

  fetch(commits) {
    fetch(`/fixtures/${commits}.json`).then(response => response.json()).then(data => {
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

export default AutolandController;
