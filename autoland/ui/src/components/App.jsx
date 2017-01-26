import React from 'react';

class App extends React.Component {
  changeDemoPage(e) {
    this.props.router.push(e.target.value);
  }

  render() {
    return (
      <div>
        <header>
          <h1>Mozilla Autoland</h1>
          <select
            defaultValue={this.props.location.pathname}
            onChange={this.changeDemoPage.bind(this)}>
              <option value="">Change Demo Page</option>
              <option value="/repos/1/series/example-01-cannot-be-landed">Example 1 Cannot be landed</option>
              <option value="/repos/1/series/example-02-can-be-landed">Example 2 Can be landed</option>
              <option value="/repos/1/series/example-03-in-progress">Example 3 In progress</option>
              <option value="/repos/1/series/example-04-landed">Example 4 Landed</option>
              <option value="/repos/1/series/example-05-failed">Example 5 Failed</option>
              <option value="/repos/1/series/fml">Example 6 Error 404</option>
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
