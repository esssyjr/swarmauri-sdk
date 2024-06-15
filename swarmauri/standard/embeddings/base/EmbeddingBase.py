from typing import Optional
from pydantic import Field
from swarmauri.core.ComponentBase import ComponentBase, ResourceTypes
from swarmauri.core.embeddings.IVectorize import IVectorize
from swarmauri.core.embeddings.IFeature import IFeature
from swarmauri.core.embeddings.ISaveModel import ISaveModel

class EmbeddingBase(IVectorize, IFeature, ISaveModel, ComponentBase):
    resource: Optional[str] =  Field(default=ResourceTypes.EMBEDDING.value, frozen=True)