/* globals $, loadFixtures */

import 'mock-ajax';
import { WelcomeMessage } from '../WelcomeMessage';

describe('Welcome Message factory', () => {
  describe('Ensure button click', () => {
    const endpointUrl = '/course/course_id/dismiss_message/';
    beforeEach(() => {
      jasmine.Ajax.install();
      loadFixtures('course_experience/fixtures/welcome-message-fragment.html');
      WelcomeMessage(endpointUrl);
    });
    afterEach(() => {
      jasmine.Ajax.uninstall();
    });
    it('When button click is made, ajax call is made and message is hidden.', () => {
      const message = document.querySelector('.welcome-message');
      document.querySelector('.dismiss-message button').dispatchEvent(new Event('click'));
      expect(jasmine.Ajax.requests.mostRecent().url).toBe(endpointUrl);
      jasmine.Ajax.requests.mostRecent().respondWith({
        status: 200,
        contentType: 'text/plain',
      });
      expect(message.innerHtml).toBe('');
    });
  });
});
