# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Submit a PySpark job to a cluster."""

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc.jobs import pyspark
from googlecloudsdk.command_lib.dataproc.jobs import submitter


@base.ReleaseTracks(base.ReleaseTrack.GA)
class PySpark(pyspark.PySparkBase, submitter.JobSubmitter):
  """Submit a PySpark job to a cluster.

  Submit a PySpark job to a cluster.

  ## EXAMPLES
  To submit a PySpark job with a local script, run:

    $ {command} --cluster my_cluster my_script.py

  To submit a Spark job that runs a script that is already on the cluster, run:

    $ {command} --cluster my_cluster file:///usr/lib/spark/examples/src/main/python/pi.py 100
  """

  @staticmethod
  def Args(parser):
    pyspark.PySparkBase.Args(parser)
    submitter.JobSubmitter.Args(parser)

  def ConfigureJob(self, messages, job, args):
    pyspark.PySparkBase.ConfigureJob(messages, job, self.files_by_type,
                                     self.BuildLoggingConfig(
                                         messages, args.driver_log_levels),
                                     args)
    submitter.JobSubmitter.ConfigureJob(messages, job, args)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class PySparkBeta(pyspark.PySparkBase, submitter.JobSubmitterBeta):
  """Submit a PySpark job to a cluster.

  Submit a PySpark job to a cluster.

  ## EXAMPLES
  To submit a PySpark job with a local script, run:

    $ {command} --cluster my_cluster my_script.py

  To submit a Spark job that runs a script that is already on the cluster, run:

    $ {command} --cluster my_cluster file:///usr/lib/spark/examples/src/main/python/pi.py 100
  """

  @staticmethod
  def Args(parser):
    pyspark.PySparkBase.Args(parser)
    submitter.JobSubmitterBeta.Args(parser)

  def ConfigureJob(self, messages, job, args):
    pyspark.PySparkBase.ConfigureJob(messages, job, self.files_by_type,
                                     self.BuildLoggingConfig(
                                         messages, args.driver_log_levels),
                                     args)
    submitter.JobSubmitterBeta.ConfigureJob(messages, job, args)


PySpark.detailed_help = {
    'EXAMPLES': """\
      To submit a PySpark job with a local script, run:

        $ {command} --cluster my_cluster my_script.py

      To submit a Spark job that runs a script that is already on the \
  cluster, run:

        $ {command} --cluster my_cluster file:///usr/lib/spark/examples/src/main/python/pi.py 100
      """,
}
PySparkBeta.detailed_help = PySpark.detailed_help
