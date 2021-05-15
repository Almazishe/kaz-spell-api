from pydantic import BaseModel


class Suggestion(BaseModel):
    term: str
    distance: int
    count: int

    class Confix:
        orm_mode = True
