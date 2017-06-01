"""
View logic for handling course welcome messages.
"""

from django.template.loader import render_to_string
from opaque_keys.edx.keys import CourseKey
from web_fragments.fragment import Fragment

from course_updates import CourseUpdatesFragmentView
from courseware.courses import get_course_info_section_module, get_course_with_access
from openedx.core.djangoapps.plugin_api.views import EdxFragmentView


class WelcomeMessageFragmentView(EdxFragmentView):
    """
    A fragment that displays a course's welcome message.
    """
    def render_to_fragment(self, request, course_id=None, **kwargs):
        """
        Renders the welcome message fragment for the specified course.

        Returns: A fragment, or None if there is no welcome message.
        """
        course_key = CourseKey.from_string(course_id)
        course = get_course_with_access(request.user, 'load', course_key, check_if_enrolled=True)
        welcome_message_html = self.welcome_message_html(request, course)
        if not welcome_message_html:
            return None

        context = {
            'welcome_message_html': welcome_message_html,
        }

        html = render_to_string('course_experience/welcome-message-fragment.html', context)
        return Fragment(html)

    @classmethod
    def welcome_message_html(cls, request, course):
        """
        Returns the course's welcome message or None if it doesn't have one.
        """
        info_module = get_course_info_section_module(request, request.user, course, 'updates')
        if not info_module:
            return None

        # Return the course update with the most recent publish date
        ordered_updates = CourseUpdatesFragmentView.order_updates(info_module.items)
        content = None
        if ordered_updates:
            info_block = getattr(info_module, '_xmodule', info_module)
            content = info_block.system.replace_urls(ordered_updates[0]['content'])

        return content
