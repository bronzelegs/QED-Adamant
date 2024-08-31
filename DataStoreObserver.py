import firebase_admin
import google.cloud.pubsub_v1 as pubsub
from firebase_admin import credentials, firestore


class DataStoreObserver:
    def __init__(self):
        self.subscriber = pubsub.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(
            "your-project-id", "simulation_results"
        )

        # Initialize Firebase
        cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.Client()

    def start(self):
        self.subscriber.subscribe(self.subscription_path, callback=self.handle_event)

    def handle_event(self, message):
        results = json.loads(message.data)
        self.store_results_in_firebase(results)

    def store_results_in_firebase(self, results):
        doc_ref = self.db.collection("simulation_results").document()
        doc_ref.set(results)
