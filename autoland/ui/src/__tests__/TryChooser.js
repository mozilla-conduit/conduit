import React from 'react';
import { shallow } from 'enzyme';

import TryChooser from '../components/TryChooser';

describe('TryChooser', () => {

  test('Changes to the try string state update the UI', () => {
    const mount = shallow(
      <TryChooser />
    );
    const tryString = 'try: test string';

    mount.setState({ tryString: tryString });
    expect(mount.find('textarea').props().value).toBe(tryString);
  });

  test('Test that clicking land runs the land callback with the try string', () => {
    const callback = jest.fn();
    const mount = shallow(
      <TryChooser landHandler={callback} />
    );
    const tryString = 'try: test string';
    mount.setState({ tryString: tryString });

    mount.find('.try-chooser-land').simulate('click');
    expect(callback.mock.calls.length).toBe(1);
    expect(callback.mock.calls[0][0]).toBe(tryString);
  });

  test('Test that clicking cancel runs the cancel callback', () => {
    const callback = jest.fn();
    const mount = shallow(
      <TryChooser cancelHandler={callback} />
    );

    mount.find('.try-chooser-cancel').simulate('click');
    expect(callback.mock.calls.length).toBe(1);
  });

});
