class Friend:
    def __init__(self, name):
        self.name = name
        self.last_invite = None

    def show_invite(self):
        return self.last_invite if self.last_invite else "No party..."


class Party:
    def __init__(self, place):
        self.place = place
        self.observers = []

    def add_friend(self, friend):
        """Add a friend to the list of observers."""
        if friend not in self.observers:
            self.observers.append(friend)

    def del_friend(self, friend):
        """Remove a friend from the list of observers."""
        if friend in self.observers:
            self.observers.remove(friend)

    def send_invites(self, time):
        """Send invitations to all observers."""
        invite_message = f"{self.place}: {time}"
        for observer in self.observers:
            observer.last_invite = invite_message


# Example: Dynamically working with methods
party = Party(input("Enter the party place: "))
while True:
    action = input("Choose an action (add, delete, send, exit): ").strip().lower()
    
    if action == "add":
        name = input("Enter friend's name to add: ")
        friend = Friend(name)
        party.add_friend(friend)
    elif action == "delete":
        name = input("Enter friend's name to delete: ")
        friend_to_remove = next((f for f in party.observers if f.name == name), None)
        if friend_to_remove:
            party.del_friend(friend_to_remove)
    elif action == "send":
        time = input("Enter the time for the invite: ")
        party.send_invites(time)
    elif action == "exit":
        break
    else:
        print("Invalid action. Please choose again.")

    # Display invites for all friends
    for friend in party.observers:
        print(f"{friend.name}: {friend.show_invite()}")

