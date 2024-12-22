# Travel Itinerary Prompt
TRAVEL_PROMPT = """
Extract these fields from the text in JSON format:
- Date of Travel
- Traveller Name (List of all passengers)
- Number of Passengers (integer count)
- Traveller Class
- Flight Time Duration
- Distance Travelled (if not available, write NA)
- Origin City
- Destination City
- Origin Airport
- Destination Airport
- Origin Airport IATA Code
- Destination Airport IATA Code

Text:
{text}

Respond strictly in JSON format.
"""

# Utility Bill Prompt
UTILITY_PROMPT = """
Extract these fields from the text in JSON format:
- Country
- Year
- Month/Period
- Total Usage (KWh)
- Total Amount (with currency)

Text:
{text}

Respond strictly in JSON format.
"""

# Fuel Bill Prompt
FUEL_PROMPT = """
Extract these fields from the text in JSON format:
- Country
- Year
- Month/Period
- Fuel Type
- Fuel Consumed (in units)
- Total Amount (with currency)

Text:
{text}

Respond strictly in JSON format.
"""
