class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)

    def publish(self, s):
        subscribers = self.subscribers[::]
        for sub in subscribers:
            cnt = sub(s)
            if cnt == 3:
                self.unsubscribe(sub)

if __name__ == '__main__':
    class Subscriber:
        def __init__(self, name, publisher):
            self.count = 0
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)

        def process(self, s):
            self.count += 1
            print("'{}' called for {} times. Message to publish: {}"
                  .format(self.name, self.count, s))
            return self.count

        def __repr__(self):
            return self.name

    publisher = Publisher()
    for i in range(5):
        subscriber_name = "Sub_" + str(i)
        Subscriber(subscriber_name, publisher)
        line = input("What to publish: ")
        publisher.publish(line)