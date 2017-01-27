import React from 'react';

import AutolandController from './AutolandController';

require('./App.css');
require('./TestApp.css');

function TestApp() {
  const fixtures = [
    { name: 'Cannot be landed', series_id: 'example-01-cannot-be-landed', repo_id: 'test-repo' },
    { name: 'Can be landed', series_id: 'example-02-can-be-landed', repo_id: 'test-repo' },
    { name: 'In progress', series_id: 'example-03-in-progress', repo_id: 'test-repo' },
    { name: 'Landed', series_id: 'example-04-landed', repo_id: 'test-repo' },
    { name: 'Failed', series_id: 'example-05-failed', repo_id: 'test-repo' },
    { name: 'Error 404', series_id: 'fml' },
  ];

  document.title = 'Autoland Test Page';

  return (
    <div>
      <header>
        <h1>Mozilla Autoland</h1>
      </header>

      <div className="app">
      {fixtures.map((fixture, i) => (
        <div key={i} className="test-case" data-title={fixture.name}>
          <AutolandController
            params={{ series_id: fixture.series_id, repo_id: fixture.repo }}/>
        </div>
      ))}
      </div>
    </div>
  );
}

export default TestApp;
