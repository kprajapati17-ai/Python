import re


def extract_contact_info(doc) -> dict:
    """
    Extract Name, Email, Phone and Location from resume text.

    Parameters:
        doc : Resume document object (must contain .text)

    Returns:
        dict : {
            "name": str | None,
            "email": str | None,
            "phone": str | None,
            "location": str | None
        }
    """

    # Default output
    info = {
        "name": None,
        "email": None,
        "phone": None,
        "location": None
    }

    try:
        # -------------------------
        # Input Validation
        # -------------------------
        if not doc or not hasattr(doc, "text"):
            return info

        full_text = doc.text.strip()

        if not full_text:
            return info

        # Split resume into lines
        lines = [line.strip() for line in full_text.splitlines() if line.strip()]

        # -------------------------
        # Compile Regex (Fast)
        # -------------------------

        email_pattern = re.compile(
            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        )

        phone_patterns = [
            re.compile(r'\+91[\s-]?(\d{5}[\s-]?\d{5})'),
            re.compile(r'\b(\d{5}[\s-]?\d{5})\b'),
            re.compile(r'(?:\+91|0)?[\s-]?(\d{10})\b')
        ]

        location_patterns = [
            re.compile(r'([A-Za-z\s]+,\s*[A-Za-z\s]+,\s*[A-Za-z\s]+)'),
            re.compile(r'([A-Za-z\s]+,\s*[A-Za-z\s]+)')
        ]

        # -------------------------
        # Extract Email
        # -------------------------

        email_match = email_pattern.search(full_text)

        if email_match:
            info["email"] = email_match.group()

        # -------------------------
        # Extract Phone
        # -------------------------

        for pattern in phone_patterns:

            mobile = pattern.search(full_text)

            if mobile:

                number = mobile.group(1)

                number = re.sub(r'[\s-]', '', number)

                if len(number) >= 10:
                    info["phone"] = number[-10:]
                    break

        # -------------------------
        # Extract Location
        # -------------------------

        for pattern in location_patterns:

            location = pattern.search(full_text)

            if location:

                info["location"] = location.group(1).strip()
                break

        # -------------------------
        # Extract Name
        # -------------------------

        ignore_words = {
            "resume",
            "curriculum vitae",
            "cv",
            "profile",
            "biodata"
        }

        for line in lines[:10]:

            clean_line = line

            clean_line = re.sub(email_pattern, "", clean_line)

            clean_line = re.sub(
                r'(\+91|0)?[\s-]?\d{5,10}',
                "",
                clean_line
            )

            clean_line = re.sub(
                r'linkedin\S*|github\S*|https?://\S*',
                "",
                clean_line,
                flags=re.IGNORECASE
            )

            clean_line = clean_line.replace("•", "").strip()

            if not clean_line:
                continue

            if clean_line.lower() in ignore_words:
                continue

            if len(clean_line.split()) <= 5:
                info["name"] = clean_line
                break

        return info

    except Exception:
        # Production:
        # logger.exception("Contact extraction failed")

        return info