import React from 'react';

import AutolandController from './AutolandController';

require('./App.css');
require('./TestApp.css');

function TestApp() {
  const fixtures = [
    { name: 'Cannot be landed', splat: 'bz://123456/cannotland', repo_id: 'mozilla-central' },
    { name: 'Can be landed', splat: 'bz://123456/canland', repo_id: 'mozilla-central' },
    { name: 'In progress', splat: 'bz://123456/inprogress', repo_id: 'mozilla-central' },
    { name: 'Landed', splat: 'bz://123456/landed', repo_id: 'mozilla-central' },
    { name: 'Failed', splat: 'bz://123456/failedland', repo_id: 'mozilla-central' },
    { name: 'Error 404', splat: 'bz://123456/fml', repo_id: 'void' },
    { name: 'Echo Series', splat: 'bz://123456/echoseries', repo_id: 'mozilla-central' },
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
            params={{ splat: fixture.splat, repo_id: fixture.repo_id }}/>
        </div>
      ))}
      </div>
    </div>
  );
}

export default TestApp;
