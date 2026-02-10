"""
Tests for moderation result classes.

These tests verify that all moderation result classes have the correct attributes
with the expected types and are properly defined as Pydantic models.
"""

import pytest
from pydantic import ValidationError

from multimodal_moderation.types.moderation_result import ModerationResult


class TestModerationResult:
    """Test the base ModerationResult class"""

    def test_has_rationale_field(self):
        """Verify ModerationResult has rationale field"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=False,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=False,
            transcription="",
        )
        assert hasattr(result, "rationale"), "ModerationResult should have a 'rationale' attribute"
        assert isinstance(result.rationale, str), "rationale should be a string"
        assert result.rationale == "Test rationale", "rationale should contain the provided value"

    def test_rationale_is_required(self):
        """Verify rationale field is required"""
        with pytest.raises(ValidationError, match="rationale"):
            ModerationResult()

    def test_is_pydantic_model(self):
        """Verify ModerationResult is a Pydantic BaseModel"""
        result = ModerationResult(
            rationale="Test",
            contains_pii=False,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=False,
            transcription="",
        )
        assert hasattr(result, "model_dump"), "ModerationResult should have model_dump method (Pydantic BaseModel)"
        assert hasattr(result, "model_validate"), "ModerationResult should have model_validate method (Pydantic BaseModel)"


class TestTextModerationResult:
    """Test the ModerationResult class"""

    def test_has_all_required_fields(self):
        """Verify ModerationResult has all required fields"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=True,
            is_disturbing=False,
            is_low_quality=False,
            transcription="",
        )

        assert hasattr(result, "rationale"), "TextModerationResult should have 'rationale' field"
        assert hasattr(result, "contains_pii"), "TextModerationResult should have 'contains_pii' field"
        assert hasattr(result, "is_unfriendly"), "TextModerationResult should have 'is_unfriendly' field"
        assert hasattr(result, "is_unprofessional"), "TextModerationResult should have 'is_unprofessional' field"

    def test_field_types(self):
        """Verify all fields have correct types"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=True,
            is_disturbing=False,
            is_low_quality=False,
            transcription="",
        )

        assert isinstance(result.rationale, str), "rationale should be a string"
        assert isinstance(result.contains_pii, bool), "contains_pii should be a boolean"
        assert isinstance(result.is_unfriendly, bool), "is_unfriendly should be a boolean"
        assert isinstance(result.is_unprofessional, bool), "is_unprofessional should be a boolean"

    def test_all_fields_are_required(self):
        """Verify all fields are required"""
        with pytest.raises(ValidationError, match="contains_pii|is_unfriendly|is_unprofessional"):
            ModerationResult(
                rationale="Test",
                is_disturbing=False,
                is_low_quality=False,
                transcription="",
            )


class TestImageModerationResult:
    """Test the ModerationResult class"""

    def test_has_all_required_fields(self):
        """Verify ModerationResult has all required fields"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=True,
            transcription="",
        )

        assert hasattr(result, "rationale"), "ImageModerationResult should have 'rationale' field"
        assert hasattr(result, "contains_pii"), "ImageModerationResult should have 'contains_pii' field"
        assert hasattr(result, "is_disturbing"), "ImageModerationResult should have 'is_disturbing' field"
        assert hasattr(result, "is_low_quality"), "ImageModerationResult should have 'is_low_quality' field"

    def test_field_types(self):
        """Verify all fields have correct types"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=True,
            transcription="",
        )

        assert isinstance(result.rationale, str), "rationale should be a string"
        assert isinstance(result.contains_pii, bool), "contains_pii should be a boolean"
        assert isinstance(result.is_disturbing, bool), "is_disturbing should be a boolean"
        assert isinstance(result.is_low_quality, bool), "is_low_quality should be a boolean"

    def test_all_fields_are_required(self):
        """Verify all fields are required"""
        with pytest.raises(ValidationError, match="contains_pii|is_disturbing|is_low_quality"):
            ModerationResult(
                rationale="Test",
                is_unfriendly=False,
                is_unprofessional=False,
                transcription="",
            )


class TestVideoModerationResult:
    """Test the ModerationResult class"""

    def test_has_all_required_fields(self):
        """Verify ModerationResult has all required fields"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=True,
            transcription="",
        )

        assert hasattr(result, "rationale"), "VideoModerationResult should have 'rationale' field"
        assert hasattr(result, "contains_pii"), "VideoModerationResult should have 'contains_pii' field"
        assert hasattr(result, "is_disturbing"), "VideoModerationResult should have 'is_disturbing' field"
        assert hasattr(result, "is_low_quality"), "VideoModerationResult should have 'is_low_quality' field"

    def test_field_types(self):
        """Verify all fields have correct types"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=False,
            is_disturbing=False,
            is_low_quality=True,
            transcription="",
        )

        assert isinstance(result.rationale, str), "rationale should be a string"
        assert isinstance(result.contains_pii, bool), "contains_pii should be a boolean"
        assert isinstance(result.is_disturbing, bool), "is_disturbing should be a boolean"
        assert isinstance(result.is_low_quality, bool), "is_low_quality should be a boolean"

    def test_all_fields_are_required(self):
        """Verify all fields are required"""
        with pytest.raises(ValidationError, match="contains_pii|is_disturbing|is_low_quality"):
            ModerationResult(
                rationale="Test",
                is_unfriendly=False,
                is_unprofessional=False,
                transcription="",
            )


class TestAudioModerationResult:
    """Test the ModerationResult class"""

    def test_has_all_required_fields(self):
        """Verify ModerationResult has all required fields"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=True,
            is_disturbing=False,
            is_low_quality=False,
            transcription="Test transcription",
        )

        assert hasattr(result, "rationale"), "AudioModerationResult should have 'rationale' field"
        assert hasattr(result, "transcription"), "AudioModerationResult should have 'transcription' field"
        assert hasattr(result, "contains_pii"), "AudioModerationResult should have 'contains_pii' field"
        assert hasattr(result, "is_unfriendly"), "AudioModerationResult should have 'is_unfriendly' field"
        assert hasattr(result, "is_unprofessional"), "AudioModerationResult should have 'is_unprofessional' field"

    def test_field_types(self):
        """Verify all fields have correct types"""
        result = ModerationResult(
            rationale="Test rationale",
            contains_pii=True,
            is_unfriendly=False,
            is_unprofessional=True,
            is_disturbing=False,
            is_low_quality=False,
            transcription="Test transcription",
        )

        assert isinstance(result.rationale, str), "rationale should be a string"
        assert isinstance(result.transcription, str), "transcription should be a string"
        assert isinstance(result.contains_pii, bool), "contains_pii should be a boolean"
        assert isinstance(result.is_unfriendly, bool), "is_unfriendly should be a boolean"
        assert isinstance(result.is_unprofessional, bool), "is_unprofessional should be a boolean"

    def test_all_fields_are_required(self):
        """Verify all fields are required"""
        with pytest.raises(ValidationError, match="transcription|contains_pii|is_unfriendly|is_unprofessional"):
            ModerationResult(
                rationale="Test",
                is_disturbing=False,
                is_low_quality=False,
                transcription="Test",
            )
