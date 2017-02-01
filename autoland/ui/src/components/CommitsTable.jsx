import React from 'react';

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

export default CommitsTable;
