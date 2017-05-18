"""
Unified course experience settings and helper methods.
"""

from django.utils.translation import ugettext as _
import waffle

from request_cache.middleware import RequestCache

# Waffle flag to enable a single unified "Course" tab.
UNIFIED_COURSE_EXPERIENCE_FLAG = 'unified_course_experience'

# Waffle flag to enable the full screen course content view
# along with a unified course home page.
UNIFIED_COURSE_VIEW_FLAG = 'unified_course_view'


def course_home_page_title(course):  # pylint: disable=unused-argument
    """
    Returns the title for the course home page.
    """
    return _('Course')


def default_course_url_name(request=None):
    """
    Returns the default course URL name for the current user.
    """
    if waffle.flag_is_active(request or RequestCache.get_current_request(), UNIFIED_COURSE_VIEW_FLAG):
        return 'openedx.course_experience.course_home'
    else:
        return 'courseware'


def course_home_url_name(request=None):
    """
    Returns the course home page's URL name for the current user.
    """
    if waffle.flag_is_active(request or RequestCache.get_current_request(), UNIFIED_COURSE_EXPERIENCE_FLAG):
        return 'openedx.course_experience.course_home'
    else:
        return 'info'
