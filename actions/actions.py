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

class ActionThrowDice1(Action):
    '''Throw a dice and sets the slot``dice_throw_1`` 
    if number is greater than or equal to `3`, does nothing otherwise.'''

    def name(self) -> Text:
        return "action_throw_dice_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = randint(1,6)
        if number >= 3:
            return [SlotSet("dice_throw_1", True)]
        else:
            return []


class ActionThrowDice2(Action):
    '''Throw a dice and sets the slot``dice_throw_2`` 
    if number is greater than or equal to `3`, does nothing otherwise.'''
    
    def name(self) -> Text:
        return "action_throw_dice_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = randint(1,6)
        if number >= 3:
            return [SlotSet("dice_throw_2", True)]
        else:
            return []

class ActionThrowDice3(Action):
    '''Throw a dice and sets the slot``dice_throw_3`` 
    if number is greater than or equal to `3`, does nothing otherwise.'''
    
    def name(self) -> Text:
        return "action_throw_dice_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = randint(1,6)
        if number >= 3:
            return [SlotSet("dice_throw_3", True)]
        else:
            return []

class ActionThrowDice4(Action):
    '''Throw a dice and sets the slot``dice_throw_4`` 
    if number is greater than or equal to `3`, does nothing otherwise.'''
    
    def name(self) -> Text:
        return "action_throw_dice_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = randint(1,6)
        if number >= 3:
            return [SlotSet("dice_throw_4", True)]
        else:
            return []

class ActioncCheckTunnelGuess1(Action):
    '''Checking the Guess entered by user. If it is in range
    ``range(1,6]``, the guess is correct, uncorrect otherwise.'''
    
    def name(self) -> Text:
        return "action_check_tunnel_lock_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Return the None value if the entity value is not set.
        g = next(tracker.get_latest_entity_values("guess_1"), None)
        
        if g is None:
            dispatcher.utter_message(text='What is your guess?')
        g = int(g)
        
        prev_slot = tracker.get_slot("dice_throw_1")
        print(prev_slot)
        if g in list(range(1,7)) and prev_slot == True:
            return [SlotSet("correct_guess_for_tunnel", True)]
        else:
            return [SlotSet("correct_guess_for_tunnel", False)]



