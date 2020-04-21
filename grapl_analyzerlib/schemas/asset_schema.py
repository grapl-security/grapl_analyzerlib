from grapl_analyzerlib.schemas.schema_builder import NodeSchema


class AssetSchema(NodeSchema):
    def __init__(self) -> None:
        super(AssetSchema, self).__init__()
        (
            self.with_str_prop("hostname")
        )
        .with_forward_edge(
            "asset_ip",
            # An asset can have multiple IP address
            OneToMany(IpAddressNodeSchema),
            "ip_assigned_to",
        )

    @staticmethod
    def self_type() -> str:
        return "Asset"
