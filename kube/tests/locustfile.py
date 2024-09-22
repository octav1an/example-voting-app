from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        headers = {"Cookies": "voter_id=9e4b36cd87b4284; Path=/"}
        data = {"vote": "b"}
        self.client.post("/", headers=headers, data=data)
