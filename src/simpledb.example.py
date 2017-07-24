from __future__ import print_function
import boto3


def quote(string):
    return string.replace("'", "''").replace('"', '""').replace('`', '``')


def put_attributes(sdb, domain, id, color):
    response = sdb.put_attributes(
        DomainName=domain,
        ItemName=id,
        Attributes=[
            {
                'Name': 'color',
                'Value': color,
                'Replace': True
            },
        ],
    )
    print(response)


if __name__ == "__main__":
    domain = "TEST_DOMAIN"
    sdb = boto3.client('sdb')
    response = sdb.create_domain(
        DomainName=domain
    )
    print(response)
    response = sdb.list_domains(
    )
    print("Current domains: %s" % response['DomainNames'])
    put_attributes(sdb, domain, "id1", "red")
    put_attributes(sdb, domain, "id2", "redblue")
    put_attributes(sdb, domain, "id3", "blue")
    response = sdb.select(
        SelectExpression='select * from %s where color like "%%%s%%"' % (domain, quote('blue')),
    )
    print(response)
    response = sdb.delete_domain(
        DomainName=domain
    )
    print(response)
