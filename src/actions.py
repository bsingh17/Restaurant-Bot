from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
import pandas as pd

dataset= pd.read_csv('dishes.csv')
dataset=dataset.set_index('dish').T.to_dict('list')
class OrderForm(FormAction):
    """Collects order information"""

    def name(self):
        return "order_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "username",
            "mailid",
            "phone_number",
            "dish_name",
            ]
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        username = tracker.get_slot("username")
        mailid = tracker.get_slot("mailid")
        phone_number=tracker.get_slot("phone_number")
        dish_name=tracker.get_slot("dish_name")
        
        
        if dish_name in dataset.keys(): 
            message="ORDER DETAILS:"+"\n\n"+"Name:"+username+"\n"+"Email:"+mailid+"\n"+"Phone Number:"+phone_number+"\n"+"Dish Name:"+dish_name+"\nThanks for ordering! Your order will be placed soon." 
            saveFile = open("some.txt", 'a')
            saveFile.write(message)
            saveFile.close()
            dispatcher.utter_message(message)
        else: 
            message="Sorry currently we are not serving this dish."    
        dispatcher.utter_message(message)
        return []