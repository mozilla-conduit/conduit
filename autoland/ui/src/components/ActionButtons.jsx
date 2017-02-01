import React from 'react';

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
    this.props.landcallback();
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

export default ActionButtons;
