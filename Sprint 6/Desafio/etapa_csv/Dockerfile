FROM jupyter/all-spark-notebook

WORKDIR app

COPY movies.csv .

EXPOSE 8888

CMD ["start-notebook.sh"]