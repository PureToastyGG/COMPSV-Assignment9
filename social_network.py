class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        new_person = Person(name)
        self.people[name] = new_person

    def add_friendship(self, person1_name, person2_name):
        person1 = self.people.get(person1_name)
        person2 = self.people.get(person2_name)
        if person1 and person2:
            person1.add_friend(person2)
            person2.add_friend(person1)
    
    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with {', '.join(friend_names)}")



# Test your code here
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends) # []
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
print(network.people) # {'Alex': <__main__.Person object at 0x1004c7380>,'Jordan': <__main__.Person object at 0x10503d810>}
network.add_person("Morgan")
network.add_person("Morgan") # Adding duplicate person
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

'''
Why is a graph the right structure to represent a social network? 
Yes, a graph is the right structure to represent a social network because it allows for efficient representation of relationships (friendships) between individuals (nodes). 
Each person can have multiple connections, and graphs can easily model these interconnecting relationships.
Why wouldn't a list or tree work as well for this?
A list or tree would not work as well because there wouldn't be as much flexibility in representing the many relationships that exist in social networks. Lists would have to
stay linear not being able to break paterns or represent multiple connections easily. Trees have a hierarchical structure that doesn't fit well with the non-hierarchical nature 
of social networks, where any person can connect to any other person without a parent-child relationship.
What performance or structural trade-offs did you notice when adding friends or printing the network?
Using a graph structure allows for efficient addition of friends and traversal of the network. Adding a friend is an O(1) operation since it involves appending to a list.
Printing the network involves iterating through each person and their friends, which is O(n + m) where n is the number of people and m is the number of friendships of each person.
'''