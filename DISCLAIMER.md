# ⚖️ Global Legal Disclaimer (全球法律免责声明)

## 1. Purpose of the Project (项目宗旨)

AISOP (AI Standard Operating Protocol) is the first protocol designed as a universal language for agentic AI. This repository provides the protocol specification, reference examples, and SDKs for building AISOP-compliant agents.

AISOP（AI 标准执行协议）是全球首个旨在作为智能体 AI 通用语言的协议。本仓库提供协议规范、参考示例和 SDK，用于构建符合 AISOP 标准的智能体。

## 2. No Warranty (不提供担保)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

软件按"原样"提供，不提供任何明示或暗示的担保。在任何情况下，作者或版权所有者均不对因软件的使用或其它交易所产生的任何索赔、损害或其它责任（无论是合同诉讼、侵权诉讼还是其它诉讼）负责。

## 3. Built-in Safety Mechanisms (内置安全机制)

AISOP is designed with constitutional-level safety guarantees defined in [SPEC.md](./SPEC.md) §1.2:

AISOP 在协议层面内置了宪法级安全保障，定义于 [SPEC.md](./SPEC.md) §1.2：

- **Human Sovereignty (人类最高主权)**: Any `sys.io.confirm` node is **inviolable** — no AI Agent, no evolutionary process, and no governance mechanism may modify, bypass, or delete it.
- **Plaintext Transparency (明文透明)**: All AISOP files must be plaintext and human-readable. Encrypted or obfuscated files are deemed invalid and the runtime must refuse execution.
- **Fractal Integrity (分形完整性)**: All sub-tasks inherit parent security constraints, including human confirmation nodes.

> [!IMPORTANT]
> These mechanisms are **protocol-level guarantees**, not optional features. However, they depend on the runtime implementation being compliant. The protocol authors make no guarantee about third-party runtime implementations.
>
> 这些机制是**协议级保障**，而非可选功能。但其有效性取决于运行时实现是否合规。协议作者不对第三方运行时实现做任何保证。

## 4. Responsibility for Agent Behavior (智能体行为责任)

As AISOP is a protocol for **autonomous or semi-autonomous agents**, the developers of this protocol have no control over the specific implementations, prompts, or actions taken by agents using this protocol. The person or entity deploying an AISOP-compliant agent is **solely responsible** for ensuring the agent's behavior complies with local laws, ethical guidelines, and safety standards.

由于 AISOP 是一个用于**自主或半自主智能体**的协议，本协议的开发者无法控制使用该协议的智能体的具体实现、提示词或行为。部署符合 AISOP 标准的智能体的人员或实体，需**独自承担**确保其行为符合当地法律、伦理准则和安全标准的全部责任。

## 5. Responsibility for Self-Evolution (自进化责任)

AISOP supports **Self-Upgrade** and **Self-Fractal** capabilities, allowing agents to autonomously rewrite their own protocol logic. When an agent evolves its AISOP:

AISOP 支持**自升级**和**自分形**能力，允许智能体自主重写自身的协议逻辑。当智能体进化其 AISOP 时：

- The **deployer** remains solely responsible for all outcomes of the evolved logic.
- The evolved AISOP must still comply with all Layer Zero Invariants ([SPEC.md](./SPEC.md) §1.2).
- Any evolution that violates Human Sovereignty or Plaintext Transparency is deemed **invalid** by the protocol.

- **部署者**仍需对进化后逻辑的所有结果承担全部责任。
- 进化后的 AISOP 仍必须符合所有不变量层公理（[SPEC.md](./SPEC.md) §1.2）。
- 任何违反人类最高主权或明文透明的进化，在协议层面均视为**无效**。

## 6. No Professional Advice (非专业建议)

Any information or logic contained within example AISOPs (e.g., stock analysis, weather reports) is for **demonstration purposes only**. It does not constitute financial, legal, or professional advice.

示例 AISOP（如股票分析、天气报告）中包含的任何信息或逻辑仅用于**演示目的**，不构成任何财务、法律或专业建议。

## 7. Right to Anonymity and Decentralization (匿名权与去中心化)

The creator of this protocol ("The Creator") reserves the right to absolute anonymity and may withdraw from the project at any time without notice. Upon withdrawal, the project shall be governed by the decentralized community under the Layer Zero Invariants and [GOVERNANCE.md](./GOVERNANCE.md), with Human Sovereignty remaining the supreme authority.

本协议的创作者（"The Creator"）保留绝对匿名的权利，并可随时退出项目而不另行通知。退出后，项目将根据不变量层和 [GOVERNANCE_zh.md](./GOVERNANCE_zh.md)，由去中心化社区治理，人类最高主权仍为最高权威。

## 8. License (许可证)

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for the full text.

本项目采用 **MIT 许可证**。完整条款请参阅 [LICENSE](./LICENSE)。

---
*By using this protocol, you acknowledge that you have read, understood, and agreed to be bound by these terms.*

*通过使用本协议，即表示您已阅读、理解并同意受上述条款约束。*
