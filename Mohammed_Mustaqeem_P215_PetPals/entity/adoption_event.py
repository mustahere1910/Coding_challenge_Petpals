class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        # Logic to host event
        pass

    def register_participant(self, participant):
        self.participants.append(participant)
