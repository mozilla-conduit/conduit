import React from 'react';

class ActionButtons extends React.Component {
  constructor(props) {
    super(props);
    this.state = { landing: false };
    this.onLandClick = this.onLandClick.bind(this);
  }

  onLandClick(e) {
    if (e) {
      e.preventDefault();
    }
    if (this.state.landing) {
      return;
    }
    this.setState({ landing: true });
    this.props.landcallback();
  }

  render() {
    let landButton;
    let tryButton;

    if (this.props.landable) {
      landButton =
        <a onClick={this.onLandClick} className="land">
          {this.state.landing ? 'Landing Commits...' : 'Land Commits'}
        </a>;
    }

    if (this.props.tryable) {
      tryButton = <a onClick={this.props.showTryChooser}>Land to Try</a>;
    }

    return (
      <div className="commit-buttons">
        {landButton}
        {tryButton}
        <a href={`https://bugzilla.mozilla.org/show_bug.cgi?id=${this.props.bug}`}>View on Bugzilla</a>
        <a href="">View on Reviewboard</a>
      </div>
    );
  }
}

export default ActionButtons;
