import React from 'react';

require('./App.css');

class App extends React.Component {
  changeDemoPage(e) {
    this.props.router.push(e.target.value);
  }

  render() {
    document.title = 'Autoland';

    return (
      <div>
        <header>
          <h1>Mozilla Autoland</h1>
          <select
            defaultValue={this.props.location.pathname}
            onChange={this.changeDemoPage.bind(this)}>
              <option value="">Change Demo Page</option>
              <option value="/repos/mozilla-central/series/bz://123456/cannotland">Example 1 Cannot be landed</option>
              <option value="/repos/mozilla-central/series/bz://123456/canland">Example 2 Can be landed</option>
              <option value="/repos/mozilla-central/series/bz://123456/inprogress">Example 3 In progress</option>
              <option value="/repos/mozilla-central/series/bz://123456/landed">Example 4 Landed</option>
              <option value="/repos/mozilla-central/series/bz://123456/failedland">Example 5 Failed</option>
              <option value="/repos/void/series/bz://123456/fml">Example 6 Error 404</option>
              <option value="/repos/mozilla-central/series/bz://123456/echoseries">Example 7 Echo Series 404</option>
          </select>
        </header>
        <div className="app">
          {this.props.children}
        </div>
      </div>
    );
  }
}

export default App;
