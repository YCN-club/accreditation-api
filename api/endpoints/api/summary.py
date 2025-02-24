from datetime import datetime
from mayim import Mayim
from sanic import Request, json
from sanic.views import HTTPMethodView

from api.decorators.require_login import require_login
from api.mayim.table_executor import TableExecutor
from api.models.internal.jwt_data import JWT_Data


class SummaryRoot(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data):
        # Get Executor
        table_executor = Mayim.get(TableExecutor)

        # Get Events
        events = await table_executor.fetch_events()
        competitve_events = await table_executor.fetch_competitive_events()
        informational_events = await table_executor.fetch_informational_events()

        # Get current year
        current_year = datetime.now().year

        # Convert Events to a dictionary
        events_dict = {event.id: event for event in events}

        # Filter and count based on year
        filtered_competitive_events = [
            event
            for event in competitve_events
            if events_dict[event.id].date.year == current_year
        ]
        filtered_informational_events = [
            event
            for event in informational_events
            if events_dict[event.id].date.year == current_year
        ]

        # Distribution of Positions for Competitive Events
        position_distribution = {}
        for event in filtered_competitive_events:
            position_distribution[event.position] = (
                position_distribution.get(event.position, 0) + 1
            )

        # Get Publication
        book_publications = await table_executor.fetch_book_publications()
        journal_publications = await table_executor.fetch_journal_publications()
        # book_publications_authors = await table_executor.fetch_book_publication_author()
        # journal_publications_authors = (
        #     await table_executor.fetch_journal_publication_author()
        # )

        # Convert Publications to a dictionary
        filtered_books = [
            publication.to_dict()
            for publication in book_publications
            if publication.year == current_year
        ]
        filtered_journals = [
            publication.to_dict()
            for publication in journal_publications
            if publication.year == current_year
        ]

        return json(
            {
                "events": {
                    "competitive": {
                        "count": len(filtered_competitive_events),
                        "events": [i.to_dict() for i in filtered_competitive_events],
                        "position_distribution": position_distribution,
                    },
                    "informational": {
                        "count": len(filtered_informational_events),
                        "events": [i.to_dict() for i in filtered_informational_events],
                    },
                },
                "publications": {
                    "book": {
                        "count": len(filtered_books),
                        "book": filtered_books,
                    },
                    "journal": {
                        "count": len(filtered_journals),
                        "journal": filtered_journals,
                    },
                },
            }
        )
