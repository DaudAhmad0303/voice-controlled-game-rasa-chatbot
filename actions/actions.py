# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from random import randint
from rasa_sdk.events import SlotSet

class ActionThrowDice(Action):

    def name(self) -> Text:
        return "action_throw_dice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         res = '''You have killed all the goblins and arrived at a secret tunnel that leads
# to necromancer's black tower. However, there is a lock on the door. From one to six
# guess the number of a single dice throw. What is your guess?'''
        number = randint(1,6)
        if number < 3:
            # dispatcher.utter_message(text=str(number) + "You were hit by the goblins' arrows and died")
            return [SlotSet("dice_throw_1", True)]
        else:
            # dispatcher.utter_message(text=res)
            return []
            

        # return []
