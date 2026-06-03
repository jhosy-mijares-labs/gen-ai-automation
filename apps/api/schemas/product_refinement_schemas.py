from pydantic import BaseModel, Field


class ProductRefinementRequest(BaseModel):
    epic_key: str = Field(
        ...,
        examples=["CARD-245"],
        description="Jira epic key to be refined.",
    )
    product_context: str = Field(
        ...,
        examples=["B2B debit card request flow for individuals and legal entities"],
        description="Business or product context used to generate the refinement.",
    )


class SuggestedJiraCard(BaseModel):
    title: str
    issue_type: str
    description: str
    acceptance_criteria: list[str]
    open_questions: list[str]
    dependencies: list[str]


class ProductRefinementResponse(BaseModel):
    epic_key: str
    summary: str
    suggested_cards: list[SuggestedJiraCard]