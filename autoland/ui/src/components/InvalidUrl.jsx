import React from 'react';

function InvalidUrl() {
  document.title = 'Page Not Found';

  return (
    <div>
      <header>
        <h1>Mozilla Autoland</h1>
      </header>

      <div className="app">
        <p>The page you requested could not be found.</p>
      </div>
    </div>
  );
}

export default InvalidUrl;
