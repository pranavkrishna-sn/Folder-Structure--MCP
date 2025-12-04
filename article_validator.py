from pydantic import validator

class ArticleValidator:
    @validator('title')
    def title_must_be_at_least_3_chars(cls, v):
        if len(v) < 3:
            raise ValueError('Title must be at least 3 characters')
        return v