import unittest
import troposphere.ec2 as ec2


class TestEC2(unittest.TestCase):

    def test_securitygroupegress(self):
        egress = ec2.SecurityGroupEgress(
            'egress',
            ToPort='80',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            'egress',
            ToPort='80',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            DestinationPrefixListId='id',
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            'egress',
            ToPort='80',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            DestinationSecurityGroupId='id',
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            'egress',
            IpProtocol="-1",
            GroupId="id",
            DestinationSecurityGroupId='id',
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            'egress',
            IpProtocol="58",
            GroupId="id",
            DestinationSecurityGroupId='id',
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            'egress',
            ToPort='80',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
            DestinationPrefixListId='id',
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test mutually exclusive fields
        egress = ec2.SecurityGroupEgress(
            'egress',
            ToPort='80',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
            DestinationPrefixListId='id',
            DestinationSecurityGroupId='id',
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test no ToPort
        egress = ec2.SecurityGroupEgress(
            'egress',
            FromPort='80',
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test no ToPort or FromPort
        egress = ec2.SecurityGroupEgress(
            'egress',
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()
