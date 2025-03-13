def asesor(req):
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "En un momento un asesor se pondra en contacto contigo. ¿Te puedo colaborar en algo mas?"]}},
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {"text": "Si"},
                                    {"text": "No"}
                                ],
                            }
                        ]
                    ]
                }
            },
        ],
    }
    return res
