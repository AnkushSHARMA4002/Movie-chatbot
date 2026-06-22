import bleach

MAX_QUERY_LENGTH = 500

def sanitize_input(query: str):

    query = bleach.clean(query)

    query = query.strip()

    if len(query) > MAX_QUERY_LENGTH:
        query = query[:MAX_QUERY_LENGTH]

    return query


def validate_query(query: str):

    if not query:
        return False

    if len(query.strip()) == 0:
        return False

    return True


def sanitize_context(context: str):

    return bleach.clean(context)