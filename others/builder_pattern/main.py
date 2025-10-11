from dataclasses import dataclass


# En vez de esto
@dataclass
class HTMLPage:
    title: str
    body: str


# Hacer esto 
class HTMLBuilder:
    page_object: HTMLPage
    title: str

    def __init__(self,title):
        self.title = title
    

    def build() -> HTMLPage:
        pass