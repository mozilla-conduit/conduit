import React from 'react';

require('./TryChooser.css');

class TryChooser extends React.Component {

  constructor(props) {
    super(props);
    this.state = { tryString: '' };
  }

  componentDidMount() {
    window.addEventListener('message', this.updateStringFromFrame);
  }

  updateStringFromFrame = event => {
    if (event.origin !== 'https://mozilla-releng.net') {
      return;
    }
    this.setState({ tryString: (event.data === '' ? '' : `try: ${event.data}`) });
  };

  updateStringFromInput = event => {
    this.setState({ tryString: event.target.value });
  };

  onLandClick = () => {
    this.props.landHandler(this.state.tryString);
  };

  onCancelClick = () => {
    this.props.cancelHandler();
  };

  render() {
    return (
      <div>
        <div className="try-chooser-overlay">
        </div>
        <div className="try-chooser">
          <div className="try-chooser-title">
            <h3>TryChooser</h3>
            <div>
              <button className="try-chooser-land" type="button"
                      onClick={this.onLandClick}>Land</button>
              <button className="try-chooser-cancel" type="button"
                      onClick={this.onCancelClick}>Cancel</button>
              <a href="https://wiki.mozilla.org/ReleaseEngineering/TryServer"
                 target="blank">What's This?</a>
            </div>
          </div>
          <div className="try-chooser-content">
            <p>Manually enter try syntax</p>
            <textarea
              rows="3"
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="off"
              spellCheck="false"
              placeholder="try: -b do -p all -u none -t none"
              onChange={this.updateStringFromInput}
              value={this.state.tryString}>
            </textarea>
          <p>Graphically build try syntax</p>
          <iframe
            src="https://mozilla-releng.net/trychooser/?embed">
          </iframe>
          </div>
        </div>
      </div>
    );
  }
}

export default TryChooser;
