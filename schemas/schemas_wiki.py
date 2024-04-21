get_search = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "title": "Wiki Search",
    "properties": {
        "pages": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "key": {"type": "string"},
                        "title": {"type": "string"},
                        "excerpt": {"type": "string"},
                        "matched_title": {
                            "anyOf": [
                                {"type": "null"},
                                {"type": "string"}
                            ]
                        },
                        "description": {"type": "string"},
                        "thumbnail": {"type": "object"}
                    },
                    "required": [
                        "id",
                        "key",
                        "title",
                        "description"
                    ]
                }
            ]
        }
    }
}

get_page = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "title": "Wiki Page",
    "properties": {
        "id": {
            "type": "number"
        },
        "key": {
            "type": "string"
        },
        "title": {
            "type": "string"
        },
        "comment": {
            "type": "string"
        },
        "latest": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                }
            }
        },
        "content_model": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "key",
        "title"
    ]
}
