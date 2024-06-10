import pymysql
import os


def read_sql_file(filename):
    """Read all lines from the SQL file."""
    with open(filename, 'r') as file:
        return file.readlines()


def execute_query(connection, query):
    """Execute the given SQL query and return the results."""
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall(), cursor.description


def sanitize_filename(filename):
    """Sanitize the filename by removing or replacing invalid characters."""
    invalid_chars = '<>:"/\\|?*\x00-\x1F'
    sanitized = ''.join('_' if c in invalid_chars else c for c in filename)
    sanitized = sanitized.strip()
    sanitized = sanitized.replace(' ', '_')
    return sanitized

def format_row(row):
    """Format each value in the row with double quotes."""
    return '\t'.join(f'"{str(value)}"' for value in row)

def export_to_txt(filename, data, headers, delimiter='\t'):
    """Export the query result to a txt file with the given delimiter."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(delimiter.join([f'"{desc[0]}"' for desc in headers]) + '\n')
        for row in data:
            file.write(format_row(row) + '\n')


def main():
    # Database connection settings
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'MySQL@123456',
        'database': 'zlib2',
        'port': 3306
    }

    # Read SQL queries from file
    sql_filename = 'sql.txt'
    queries = read_sql_file(sql_filename)
    if not queries:
        print("SQL file is empty or not found.")
        return

    # Connect to the database
    connection = pymysql.connect(**db_config)

    try:
        for query in queries:
            query = query.strip()
            if query:  # Only process non-empty lines
                # Execute the query
                fullQuery = ('SELECT zlibrary_id, extension, title FROM books '
                             + query +
                             ' ORDER BY zlibrary_id ASC;')
                print(f"fullQuery= {fullQuery}")

                data, headers = execute_query(connection, fullQuery)

                # Get the number of rows returned
                row_count = len(data)

                # Sanitize the filename
                base_filename = sanitize_filename(query)[:50]
                output_filename = f"{base_filename}（总：{row_count}）.txt"

                # Export the results to a txt file
                export_to_txt(output_filename, data, headers)

                print(f"Query results exported to {output_filename}")

    finally:
        connection.close()


if __name__ == '__main__':
    main()
