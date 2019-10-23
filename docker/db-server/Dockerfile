FROM postgres

# Maintainer info
LABEL maintainer="@code-monk08"

# Add init script
ADD ./db/init.sql /docker-entrypoint-initdb.d/
