from grapl_analyzerlib.schemas.schema_builder import NodeSchema, ManyToOne


class NetworkConnectionSchema(NodeSchema):
    def __init__(self) -> None:
        super(NetworkConnectionSchema, self).__init__()
        (
            self.with_str_prop("src_ip_address")
            .with_str_prop("src_port")
            .with_str_prop("dst_ip_address")
            .with_str_prop("dst_port")
            .with_int_prop("created_timestamp")
            .with_int_prop("terminated_timestamp")
            .with_int_prop("last_seen_timestamp")
            .with_forward_edge(
                "inbound_network_connection_to",
                ManyToOne(IpPortSchema),
                "network_connections_from",
            )
        )

    @staticmethod
    def self_type() -> str:
        return "NetworkConnection"


from grapl_analyzerlib.schemas.ip_port_schema import IpPortSchema
