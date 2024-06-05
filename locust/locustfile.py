from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_fastapi(self):
        self.client.get("http://fastapi:8000/", name="FastAPI Root")

    @task
    def get_flask(self):
        self.client.get("http://flask:5000/", name="Flask Root")

