import os
import xml.dom.minidom as xml
import logging


def load_pref_entries(path='/home/leapset/.java/.userPrefs/CincoTinyServer/prefs.xml'):
    """
    load given file
    :param path: path of file
    :return: entries
    """
    try:
        if not os.path.exists(path):
            return {}

        # parse the XML file 'entry' elements. All of the preference
        preference_entries = xml.parse(path).getElementsByTagName('entry')
        return preference_entries

    except Exception as exception:
        logging.exception("Error while getting preference data from pref.xml file: %s", exception)
        return None


print load_pref_entries()
