# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import os
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from server.github import search_first_repo_with_name


class RepositoryForm(FormAction):

    def name(self) -> Text:
        return "repository_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["repository_name"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "repository_name": [
                self.from_entity(
                    entity="repository_name", intent=["request_repository", "inform_repository"]
                ),
                self.from_text(intent=["inform_repository"])
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        repo = search_first_repo_with_name(tracker.get_slot("repository_name"))

        # utter submit template
        dispatcher.utter_message(text='''\
I've found {repo.name}, {repo.stargazers_count}🟊 (stars), {repo.forks_count}ᛦ (forks)
{repo.description}
{repo.clone_url}
    '''.format(**locals()))
        return self.deactivate()
