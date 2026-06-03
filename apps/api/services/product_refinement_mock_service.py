from apps.api.schemas.product_refinement_schemas import (
    ProductRefinementRequest,
    ProductRefinementResponse,
    SuggestedJiraCard,
)


def generate_mock_product_refinement(
    request: ProductRefinementRequest,
) -> ProductRefinementResponse:
    return ProductRefinementResponse(
        epic_key=request.epic_key,
        summary=(
            "Mock product refinement generated from the provided epic and product context. "
            "This response simulates how the future AI workflow will analyze business needs, "
            "identify flows, and suggest actionable Jira cards."
        ),
        suggested_cards=[
            SuggestedJiraCard(
                title="Define applicant type for debit card request",
                issue_type="Story",
                description=(
                    "As a Product Owner, I want the system to identify whether the debit card "
                    "request is for an individual or a legal entity, so that the correct flow, "
                    "required information, and validation rules can be applied."
                ),
                acceptance_criteria=[
                    "Given a B2B client starts a debit card request, when the flow begins, then the system must ask for the applicant type.",
                    "Given the applicant type is individual, when the user continues, then the system must request individual-specific information.",
                    "Given the applicant type is legal entity, when the user continues, then the system must request company and legal representative information.",
                ],
                open_questions=[
                    "Should the applicant type be selected manually or inferred from existing client data?",
                    "Are both individual and legal entity flows available for all B2B clients?",
                ],
                dependencies=[
                    "Definition of required fields for individuals.",
                    "Definition of required fields for legal entities.",
                    "Business rules for B2B debit card eligibility.",
                ],
            )
        ],
    )