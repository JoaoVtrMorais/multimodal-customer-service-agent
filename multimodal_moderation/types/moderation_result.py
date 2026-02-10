from pydantic import BaseModel, Field


class ModerationResult(BaseModel):
    rationale: str = Field(description="Explanation of what was harmful and why")

    contains_pii: bool = Field(
        description="Whether the content contains any personally-identifiable information (PII)"
    )

    is_unfriendly: bool = Field(
        description="Whether unfriendly tone or content was detected"
    )

    is_unprofessional: bool = Field(
        description="Whether unprofessional tone or content was detected"
    )

    is_disturbing: bool = Field(
        description="Whether content is disturbing (image/video)"
    )

    is_low_quality: bool = Field(
        description="Whether content quality is low (image/video)"
    )

    transcription: str = Field(description="Audio transcription if available")
