import time


class Producer:
    """Define the 'resource-intensive' object to instantiate"""

    def produce(self):
        print("producer is working hard")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Defines the relatively less 'resource-intensive' proxy to instantiate"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist check if Producer is available ..")

        if self.occupied == "No":
            # if the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # make the producer meet the guest
            self.producer.meet()
        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


# instantiate a proxy
p = Proxy()

# make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = "Yes"

# Make the Producer produce
p.produce()
