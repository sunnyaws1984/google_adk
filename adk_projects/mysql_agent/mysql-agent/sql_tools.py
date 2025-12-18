from sqlalchemy import create_engine, text

db = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/company?ssl_disabled=true")

def run_sql(query: str) -> dict:
    """
    Executes SQL and returns ADK-compatible tool response.
    """
    try:
        with db.connect() as conn:
            result = conn.execute(text(query)).mappings().fetchall()
            rows = [dict(row) for row in result]

        return {
            "result": {
                "status": "success",
                "rows": rows
            }
        }

    except Exception as e:
        return {
            "result": {
                "status": "error",
                "error_message": str(e)
            }
        }