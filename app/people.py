#!/usr/bin/env python
import requests
import copy


class People:

    def fetchPeople(self):
        """
        :author: Gaurav Singh
        :description: fetch people details for each movie
        :return: people data
        """
        people = None
        api_endpoint_people = "https://ghibliapi.herokuapp.com/people"

        try:
            response = requests.get(api_endpoint_people)
            print(f"Endpoint /people Response Status code is: {response}")
            response.raise_for_status()
        except requests.exceptions.RequestException as exception:
            print(f"Exception is: {exception}")
            raise SystemExit(exception)
        else:
            people = response.json()

        return people

    def build_dict_id_people(self, people):
        """
        :author: Gaurav Singh
        :param people: people
        :return: return peopleid dictionary
        :decription: This method is just to build and return peopleid dict
        """

        peopleid = {}
        for p in people:
            if "films" in p:
                for id in p["films"]:
                    if id in peopleid:
                        peopleid[id].append(p["name"])
                    else:
                        peopleid[id] = [p["name"]]
        return peopleid

    def filmPeopleID(self, people_list):
        """
        :param people_list:
        :author: Gaurav Singh
        :param people: people
        :return: return mapped film id for people
        :description: This method is just to map people id for each movie
        and return film people id
        """

        for p in people_list:
            if "films" in p:
                p["films"] = list(map(lambda x: x.split("/")[-1], p["films"]))
        filmpeopleid = self.build_dict_id_people(people_list)
        return filmpeopleid
