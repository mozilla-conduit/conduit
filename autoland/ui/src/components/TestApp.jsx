import React from 'react';

import AutolandController from './AutolandController';

require('./App.css');
require('./TestApp.css');

function TestApp() {
  const fixtures = [
    { name: 'Cannot be landed', splat: 'bz://123456/cannotland', repoId: 'mozilla-central' },
    { name: 'Can be landed', splat: 'bz://123456/canland', repoId: 'mozilla-central' },
    { name: 'In progress', splat: 'bz://123456/inprogress', repoId: 'mozilla-central' },
    { name: 'Landed', splat: 'bz://123456/landed', repoId: 'mozilla-central' },
    { name: 'Failed', splat: 'bz://123456/failedland', repoId: 'mozilla-central' },
    { name: 'Error 404', splat: 'bz://123456/fml', repoId: 'void' },
    { name: 'Echo Series', splat: 'bz://123456/echoseries', repoId: 'mozilla-central' },
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
            params={{ splat: fixture.splat, repoId: fixture.repoId }}/>
        </div>
      ))}
      </div>
    </div>
  );
}

export default TestApp;
